# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
	config.vm.box = "dook/debian-python"
    config.vm.network 'forwarded_port', guest: 8000, host: 8000

    config.vm.provider 'virtualbox' do |vb|
        vb.memory = '512'
        vb.customize [
            'modifyvm', :id, '--natdnsproxy1', 'on', '--natdnshostresolver1', 'on',
            '--nictype1', '82543GC', '--nictype2', '82543GC'
        ]
    end

    config.vm.provision 'shell', path: 'bin/setup'
end
